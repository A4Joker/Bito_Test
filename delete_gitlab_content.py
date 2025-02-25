import requests
import sys

def delete_issue_content(gitlab_url, project_id, token):
    headers = {
        'PRIVATE-TOKEN': token
    }
    
    # Get all issues in the project
    issues_url = f"{gitlab_url}/api/v4/projects/{project_id}/issues"
    issues_response = requests.get(issues_url, headers=headers)
    
    if issues_response.status_code != 200:
        print(f"Failed to fetch issues. Status code: {issues_response.status_code}")
        return
    
    issues = issues_response.json()
    
    for issue in issues:
        issue_iid = issue['iid']
        
        # Clear issue description
        update_url = f"{gitlab_url}/api/v4/projects/{project_id}/issues/{issue_iid}"
        update_data = {'description': ''}
        update_response = requests.put(update_url, headers=headers, json=update_data)
        
        if update_response.status_code == 200:
            print(f"Cleared description for issue #{issue_iid}")
        else:
            print(f"Failed to clear description for issue #{issue_iid}")
        
        # Get and delete all comments
        comments_url = f"{gitlab_url}/api/v4/projects/{project_id}/issues/{issue_iid}/notes"
        comments_response = requests.get(comments_url, headers=headers)
        
        if comments_response.status_code == 200:
            comments = comments_response.json()
            for comment in comments:
                delete_url = f"{gitlab_url}/api/v4/projects/{project_id}/issues/{issue_iid}/notes/{comment['id']}"
                delete_response = requests.delete(delete_url, headers=headers)
                
                if delete_response.status_code == 204:
                    print(f"Deleted comment {comment['id']} from issue #{issue_iid}")
                else:
                    print(f"Failed to delete comment {comment['id']} from issue #{issue_iid}")
        else:
            print(f"Failed to fetch comments for issue #{issue_iid}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python delete_gitlab_content.py <gitlab_url> <project_id> <access_token>")
        sys.exit(1)
    
   gitlab_url = sys.argv[1]
   project_id = sys.argv[2]
   token = sys.argv[3]
    
    try:
        project_id = int(project_id)
    except ValueError:
        print("Error: project_id must be an integer")
        sys.exit(1)
    if not gitlab_url.startswith(('http://', 'https://')):
        print("Error: gitlab_url must be a valid URL starting with http:// or https://")
        sys.exit(1)
    
    delete_issue_content(gitlab_url, project_id, token)

if __name__ == "__main__":
    main()