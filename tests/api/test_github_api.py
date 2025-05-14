import pytest
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

@pytest.mark.emojis
def test_github_empjis(github_api):
    r = github_api.recieve_emojis()
   # assert r.status_code == 200
    # print(r["+1"])
    assert  (len(r)) != 0
    assert (r["+1"]) == "https://github.githubassets.com/images/icons/emoji/unicode/1f44d.png?v8"
    assert (r["ukraine"]) == "https://github.githubassets.com/images/icons/emoji/unicode/1f1fa-1f1e6.png?v8"
    assert (r["israel"]) == "https://github.githubassets.com/images/icons/emoji/unicode/1f1ee-1f1f1.png?v8"
    assert (r["zzz"]) == "https://github.githubassets.com/images/icons/emoji/unicode/1f4a4.png?v8"

@pytest.mark.commits
def test_search_existing_commits(github_api):
    r = github_api.search_commits("juliakrmn", "Python_Project")

    # assert (r["email"]) == "korman.julia@gmail.com"
    assert len(r) != 0
    for commit in r:
        assert len(commit["sha"]) == 40
       # assert (commit["message"]) != ""
        assert (commit["author"]) == {"name", "email", "date"}

    #print (r[0]["sha"])

@pytest.mark.commits
def test_status_code_of_existing_commits(github_api):
    status_code = github_api.search_status_code("juliakrmn", "Python_Project")
#     # assert (r["author"]) == "Julia Korman"
#     # assert (r["email"]) == "korman.julia@gmail.com"
#     # assert (r["commits"]) != 0
    assert(status_code) == 200

@pytest.mark.commits
def test_commits_with_parameters(github_api):
    commit = github_api.commits_work_with_parameters("juliakrmn", "Python_Project", "Julia Korman")
    assert(commit.status_code) == 200


@pytest.mark.commits
def test_search_non_existing_commits(github_api):
    r = github_api.search_commits("juliakorman1", "")

    # assert (r["email"]) == "korman.julia@gmail.com"
    # print (len(r))
    assert(r["documentation_url"]) == "https://docs.github.com/rest"
    assert (r["message"]) == "Not Found"
    assert (r["status"]) == "404"

@pytest.mark.commits
def test_commits_expected_results(github_api):
    commit = github_api.commits_work_with_parameters("octocat", "Hello-World", "" )
    assert(commit.status_code) == 200
  #  assert len(commit["sha"]) == 40


# print("Status code:", status)
# print("Rate limit:", headers.get("X-RateLimit-Remaining"))
# print("First SHA:", commits[0]["sha"] if commits else "No commits found")