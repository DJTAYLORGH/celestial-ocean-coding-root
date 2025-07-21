from threat_journal import ThreatJournal, catalog_entry

# ... after identifying suspects ...
tj = ThreatJournal("threat_journal.yaml")

for repo in suspects:
    entry = catalog_entry(repo)     # from your scan script
    if tj.add_entry(entry):
        print(f"Cataloged: {repo['full_name']}")