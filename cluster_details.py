def top_hashtags_per_cluster(cluster, unique_terms):

	top_hash_words = []

	top_tags = cluster.argsort()[-20:][::-1]

	for i in top_tags:
		top_hash_words.append(unique_terms[i])
	print(top_hash_words)

	word_frequency = Counter(top_hash_words)
	print(word_frequency)

def top_urls_per_cluster():
	top_urls = []

	

def top_mentions_per_cluster():
