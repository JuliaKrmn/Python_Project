export class GitHubLoginPage {
    goTo() {
      cy.visit('https://github.com/login')
    }
  
    tryLogin(username, password) {
      cy.get('#login_field').type(username)
      cy.get('#password').type(password)
      cy.get('input[type="submit"]').click()
    }
  
    checkTitle(expectedTitle) {
      cy.title().should('eq', expectedTitle)
    }
  }