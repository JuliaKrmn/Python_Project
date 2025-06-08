import { GitHubLoginPage } from '../support/pages/GitHubLoginPage'

describe('GitHub Login UI', () => {
  it('should show error for incorrect credentials', () => {
    const login = new GitHubLoginPage()
    login.goTo()
    login.tryLogin('page_objects@hotmail.com', 'wrong_password')
    login.checkTitle('Sign in to GitHub · GitHub')
  })
})