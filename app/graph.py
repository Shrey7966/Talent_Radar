import networkx as nx

def build_skill_graph():
    G = nx.Graph()

    edges = [
        ("python", "machine learning"),
        ("python", "data analysis"),
        ("aws", "cloud"),
        ("docker", "kubernetes"),
        ("devops", "docker"),
        ("devops", "aws"),
        ("cloud", "terraform"),
    ]

    G.add_edges_from(edges)

    return G


def recommend_skills(existing_skills, G):
    recommendations = set()

    for skill in existing_skills:
        if skill in G:
            neighbors = list(G.neighbors(skill))
            recommendations.update(neighbors)

    return list(recommendations)