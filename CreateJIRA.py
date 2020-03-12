import csv
from CommonUtils import read_input

issueList, _ = read_input()

features = []
for issue in issueList:
    features.append(issue[-2])

features = list(set(features))

with open('jira_issues.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Issue Type", "Summary", "Epic Name", "Epic Link", "Description", "Story Points"])
    for feature in features:
        writer.writerow(["Epic", "Epic for feature number " + feature, feature, "", "", ""])
    for issue in issueList:
        description = issue[1]

        # Add bullet points
        # \\\\ is necessary to create multi-line description in JIRA
        if len(issue[2]) > 0:
            description += "\n * " + "\n * ".join(issue[2])
        writer.writerow(["Story", issue[0], "", issue[-2], description, issue[3]])
        # TODO: Create Epics in JIRA and issue types for Story and Epic -write a unit test for this
        if len(issue[3]) > 0:
            description += "\n * " + "\n * ".join(issue[3])
        writer.writerow(["Story", issue[0], "", issue[-3], description, issue[4]])  # Continue the append of issues to
        # allow multi-line comment in JIRA

        # A generalized procedure for adding multi-line descriptions in JIRA
        while len(issueList) > 0:
            description += "\n * " + "\n * ".join(issue[issue])
            writer.writerow(["Story", issue[issue], "", issue[issue], description, issue[issue]])
