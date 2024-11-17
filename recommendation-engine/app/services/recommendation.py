def get_recommendations(user_id, redis_client):
    # Check if recommendations are in cache first
    cached_recs = redis_client.get(f'recs:{user_id}')
    if cached_recs:
        return cached_recs.decode('utf-8').split(',')

    # Placeholder for algorithm (to be added later)
    recommendations = ['Product 1', 'Product 2', 'Product 3']

    # Cache the recommendations for future use
    redis_client.set(f'recs:{user_id}', ','.join(recommendations), ex=3600)

    return recommendations
