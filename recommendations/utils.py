import torch
from sentence_transformers import SentenceTransformer

# Model Yükleme
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')

def match_category_with_embeddings(user_input, categories, weights):
    input_embedding = model.encode(user_input, convert_to_tensor=True)
    category_scores = {}
    for category, keywords in categories.items():
        category_embedding = model.encode(keywords, convert_to_tensor=True)
        similarity_score = torch.matmul(input_embedding, category_embedding.T).item()
        weighted_score = similarity_score * weights.get(category, 1.0)
        category_scores[category] = weighted_score
    return max(category_scores, key=category_scores.get)

def calculate_course_scores(courses, user_input):
    query_embedding = model.encode([user_input], convert_to_tensor=True)
    course_embeddings = model.encode(courses, convert_to_tensor=True)
    dot_products = torch.matmul(course_embeddings, query_embedding.T).flatten().cpu().numpy()
    normalized_scores = (dot_products - dot_products.min()) / (dot_products.max() - dot_products.min())
    return normalized_scores
