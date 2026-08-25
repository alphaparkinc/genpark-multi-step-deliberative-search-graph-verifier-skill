from client import MultiStepDeliberativeSearchGraphVerifierClient

def main():
    client = MultiStepDeliberativeSearchGraphVerifierClient()
    res = client.execute_deliberative_search_tree('Solid-state electrolyte ionic conductivity limits in garnet ceramics', 4)
    print('Search Tree: ' + res['search_tree_id'] + ' | ' + res['hypothesis'])
    print('Sub-queries: ' + str(res['sub_queries_decomposed']) + ' | Verified Citations: ' + str(res['peer_reviewed_citations_verified']))
    print('Consensus Score: ' + str(res['cross_evidence_consensus_score_pct']) + '% (Confidence: ' + str(res['epistemic_confidence_index']) + ')')
    print('Report URL: ' + res['synthesis_markdown_report_url'])

if __name__ == '__main__':
    main()
