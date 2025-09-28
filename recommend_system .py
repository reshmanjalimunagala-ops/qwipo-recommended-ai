# Function to recommend products based on input item
def recommend_products(rules, product_name, top_n=3):
    recommendations = rules[rules['antecedents'].apply(lambda x: product_name in x)]
    recommendations = recommendations.sort_values(by='lift', ascending=False)
    
    # Get the top N recommended products
    recommended_items = []
    for _, row in recommendations.iterrows():
        for item in row['consequents']:
            if item != product_name and item not in recommended_items:
                recommended_items.append(item)
                if len(recommended_items) >= top_n:
                    break
        if len(recommended_items) >= top_n:
            break
    return recommended_items
  # Example: Recommend products for 'Milk'
product_to_check = 'Milk'
recommended = recommend_products(rules, product_to_check)
print(f"Products frequently bought with {product_to_check}: {recommended}")
