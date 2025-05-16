from jsonschema import validate
import pytest

from modules.api.clients.github import GitHub
#from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    #api = GitHub()
    # user = api.get_user_defunkt()
    user = github_api.get_user ("defunkt")
    assert user["login"] == "defunkt"

@pytest.mark.api
def test_non_exist_user(github_api):
   # api = GitHub()
    # message = api.get_non_exist_user()
    # assert message["status"] == "404"
    # r = api.get_non_exist_user()
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"
    #print(r)


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become_qa_auto")
    assert r["total_count"] == 57
    assert "become-qa-auto-aug2020" in r["items"][0]["name"]

@pytest.mark.api
def test_repo_doesnt_exist(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0

@pytest.mark.api
def test_repo_with_single_char_can_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0

#-------------Emojis API from GitHub------------------------------

@pytest.mark.emojis
def test_github_emojis(github_api):
    r = github_api.recieve_emojis()
    assert github_api.get_emojis_status() == 200
    print(r["+1"]) 
    assert  (len(r)) != 0

@pytest.mark.emojis
def test_known_emojis(github_api):
    r = github_api.recieve_emojis()
    known_emojis = ["+1", "ukraine", "israel", "zzz"]    

    for emojis in known_emojis:
        assert emojis in r
        assert r[emojis].startswith("https://github.githubassets.com/images/icons/emoji/unicode/")
        assert r[emojis].endswith(".png?v8")
    
    #This is simplified way to verify certain emoji:
    assert (r["accordion"]) == "https://github.githubassets.com/images/icons/emoji/unicode/1fa97.png?v8"


@pytest.mark.emojis
def test_emojis_wrong_url(github_api):
    r = github_api.nonexisting_emoji_status() 
    assert r.status_code  == 404
    response_text = r.json()  
    assert "message" in response_text
    assert response_text["message"] == "Not Found"

#Call a json schema to compare
@pytest.mark.emojis
def test_compare_emojisschema_with_fileschema(github_api):
    saved_schema = GitHub.load_emojis_expected_schema()
    api_responce = github_api.recieve_emojis()
    validate (instance=api_responce, schema=saved_schema)


#-----------------Commits API from Github --------------------------------------------------------------------------------
@pytest.mark.commits
def test_search_existing_commits(github_api):
    r = github_api.search_commits("juliakrmn", "Python_Project")

    assert isinstance(r, list)
    assert len(r) > 0

    for commit in r:
        assert "sha" in commit
        assert len(commit["sha"]) == 40

        # Navigate nested fields
        commit_data = commit.get("commit", {})
        assert "message" in commit_data
        assert commit_data["message"] != ""

        author_info = commit_data.get("author", {})
        for key in {"name", "email", "date"}:
            assert key in author_info

#Status codes
@pytest.mark.commits
def test_status_code_of_existing_commits(github_api): 
    status_code = github_api.search_status_code("juliakrmn", "Python_Project")
    assert(status_code) == 200

@pytest.mark.commits
def test_status_code_404_commits(github_api):
    status_code = github_api.search_status_code("juliakrmn404", "Python_Project")
    assert(status_code) == 404

@pytest.mark.commits
def test_status_empty_repo(github_api):
    status_code = github_api.search_status_code("juliakrmn", "empty_repo")
    assert(status_code) == 409

#API with parameters
@pytest.mark.commits
def test_commits_with_parameters(github_api):
    commit = github_api.commits_work_with_parameters("juliakrmn", "Python_Project", "Julia Korman")
    assert(commit.status_code) == 200

@pytest.mark.commits
def test_commits_expected_results(github_api):
    commit = github_api.commits_work_with_parameters("octocat", "Hello-World", "" )
    assert(commit.status_code) == 200
  #  assert len(commit["sha"]) == 40

#API request with extention
@pytest.mark.commits
def test_commits_expected_results(github_api):
    commit = github_api.commits_where_head_is("juliakrmn", "Python_Project",  "2fc4477f6ae2f52d397cdb975f5c8a0578b5b522" )
    assert(commit.status_code) == 200

#Negative tests
@pytest.mark.commits
def test_search_non_existing_commits(github_api):
    r = github_api.search_commits("juliakorman1", "")
    assert(r["documentation_url"]) == "https://docs.github.com/rest"
    assert (r["message"]) == "Not Found"
    assert (r["status"]) == "404"

#Call a whole file to compare
@pytest.mark.commits
def test_compare_api_with_file(github_api):
    expected = GitHub.load_expected_commits()
    api_responce = github_api.search_commits("juliakrmn", "Python_Project")
    assert api_responce == expected

#Compare structure of .json on file and in API 
@pytest.mark.commits
def test_compare_setapi_with_setfile(github_api):
    expected = GitHub.load_expected_commits()
    api_responce = github_api.search_commits("juliakrmn", "Python_Project")

    for expected, api_responce in zip(expected, api_responce):
        assert set(api_responce.keys()) == set(expected.keys())


# print("Status code:", status)
# print("Rate limit:", headers.get("X-RateLimit-Remaining"))
# print("First SHA:", commits[0]["sha"] if commits else "No commits found")


#     # assert (r["author"]) == "Julia Korman"
#     # assert (r["email"]) == "korman.julia@gmail.com"
#     # assert (r["commits"]) != 0


