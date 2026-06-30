import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# 1. SIMULAÇÃO DE BANCO DE DADOS (DATA SETS)
# ==========================================

# Catálogo de Filmes (Metadados para Filtragem Baseada em Conteúdo)
movies_data = {
    'movie_id': [1, 2, 3, 4, 5, 6],
    'title': ['The Matrix', 'Inception', 'Interstellar', 'The Godfather', 'Pulp Fiction', 'Goodfellas'],
    'genres': ['Sci-Fi Action Cyberpunk', 'Sci-Fi Thriller Mind-bending', 'Sci-Fi Drama Space', 'Crime Drama Classic', 'Crime Thriller Cult', 'Crime Biography Drama'],
    'director': ['Wachowskis', 'Christopher Nolan', 'Christopher Nolan', 'Francis Ford Coppola', 'Quentin Tarantino', 'Martin Scorsese']
}

# Matriz de Avaliações de Usuários (Para Filtragem Colaborativa)
# Linhas: Usuários (User_A até User_E), Colunas: Filmes (ID 1 a 6). 0 significa que não assistiu.
ratings_data = {
    'user_id': ['User_A', 'User_B', 'User_C', 'User_D', 'User_E'],
    1: [5, 4, 0, 1, 0], # Matrix
    2: [4, 0, 5, 1, 2], # Inception
    3: [0, 5, 4, 0, 1], # Interstellar
    4: [1, 2, 0, 5, 5], # Godfather
    5: [2, 0, 1, 4, 5], # Pulp Fiction
    6: [0, 1, 2, 5, 4]  # Goodfellas
}

df_movies = pd.DataFrame(movies_data)
df_ratings = pd.DataFrame(ratings_data).set_index('user_id')

# ==========================================
# 2. MOTOR DE FILTRAGEM BASEADA EM CONTEÚDO
# ==========================================
class ContentBasedRecommender:
    def __init__(self, movies_df):
        self.movies_df = movies_df
        self.similarity_matrix = None
        
    def compute_similarity(self):
        # Combina gêneros e diretores para criar um "sopa de palavras" (metadata soup)
        self.movies_df['metadata'] = self.movies_df['genres'] + " " + self.movies_df['director']
        
        # Vetorização TF-IDF (Frequência do Termo - Inverso da Frequência nos Documentos)
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.movies_df['metadata'])
        
        # Calcula a Similaridade de Cosseno entre os vetores dos filmes
        self.similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
        
    def get_recommendations(self, movie_title, top_n=2):
        if self.similarity_matrix is None:
            self.compute_similarity()
            
        # Pega o índice do filme target
        idx = self.movies_df[self.movies_df['title'] == movie_title].index[0]
        
        # Pares de (índice, pontuação de similaridade)
        sim_scores = list(enumerate(self.similarity_matrix[idx]))
        
        # Ordena baseado na pontuação (decrescente) e remove o próprio filme
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = [score for score in sim_scores if score[0] != idx]
        
        # Retorna os top N filmes mais parecidos
        top_indices = [score[0] for score in sim_scores[:top_n]]
        return self.movies_df.iloc[top_indices][['title', 'genres']]

# ==========================================
# 3. MOTOR DE FILTRAGEM COLABORATIVA (USER-ITEM)
# ==========================================
class CollaborativeReminder:
    def __init__(self, ratings_df):
        self.ratings_df = ratings_df
        self.user_similarity = None
        
    def compute_user_similarity(self):
        # Calcula a similaridade entre usuários baseada nas notas dadas
        self.user_similarity = cosine_similarity(self.ratings_df)
        self.user_similarity_df = pd.DataFrame(
            self.user_similarity, 
            index=self.ratings_df.index, 
            columns=self.ratings_df.index
        )
        
    def predict_rating(self, user_id, movie_id):
        if self.user_similarity is None:
            self.compute_user_similarity()
            
        # Se o usuário já avaliou o filme, retorna a nota real
        if self.ratings_df.loc[user_id, movie_id] > 0:
            return self.ratings_df.loc[user_id, movie_id]
            
        # Caso contrário, prevê a nota baseada em usuários similares
        similar_users = self.user_similarity_df[user_id].drop(user_id)
        other_user_ratings = self.ratings_df[movie_id].drop(user_id)
        
        # Ignora usuários que não avaliaram esse filme (nota = 0)
        valid_indices = other_user_ratings > 0
        if not valid_indices.any():
            return self.ratings_df.loc[user_id].mean() # Fallback para a média do usuário
            
        numerator = np.dot(similar_users[valid_indices], other_user_ratings[valid_indices])
        denominator = np.sum(np.abs(similar_users[valid_indices]))
        
        if denominator == 0:
            return 0
            
        return numerator / denominator

# ==========================================
# 4. ORQUESTRAÇÃO E EXECUÇÃO DO SISTEMA
# ==========================================
if __name__ == "__main__":
    print("="*60)
    print(" INICIALIZANDO ENGINE HÍBRIDA DE RECOMENDAÇÃO ".center(60, "#"))
    print("="*60, "\n")
    
    # --- Testando Baseado em Conteúdo ---
    print("[1] Testando: Filtragem Baseada em Conteúdo")
    content_eng = ContentBasedRecommender(df_movies)
    target_movie = "Inception"
    recs_content = content_eng.get_recommendations(target_movie, top_n=2)
    
    print(f"Porque você assistiu '{target_movie}', você pode gostar de:")
    print(recs_content.to_string(index=False), "\n")
    print("-" * 60)
    
    # --- Testando Filtragem Colaborativa ---
    print("[2] Testando: Filtragem Colaborativa (Predição de Nota)")
    collab_eng = CollaborativeRecommender(df_ratings)
    
    target_user = "User_A"
    target_movie_id = 3 # Interstellar (User_A não assistiu esse filme no dataset)
    movie_name = df_movies[df_movies['movie_id'] == target_movie_id]['title'].values[0]
    
    predicted_score = collab_eng.predict_rating(target_user, target_movie_id)
    print(f"Previsão de nota para {target_user} no filme '{movie_name}': {predicted_score:.2f} / 5.0")
    
    # --- Gerando Lista de Recomendação Completa para o Usuário ---
    print("\n[3] Gerando Recomendações Personalizadas...")
    user_unwatched_movies = df_ratings.loc[target_user][df_ratings.loc[target_user] == 0].index
    
    predictions = {}
    for m_id in user_unwatched_movies:
        m_name = df_movies[df_movies['movie_id'] == m_id]['title'].values[0]
        predictions[m_name] = collab_eng.predict_rating(target_user, m_id)
        
    sorted_predictions = sorted(predictions.items(), key=lambda x: x[1], reverse=True)
    print(f"\nRanking de recomendações para {target_user} (Filmes não assistidos):")
    for movie, score in sorted_predictions:
        print(f" -> {movie}: Nota prevista {score:.2f}")
    print("\n" + "="*60)