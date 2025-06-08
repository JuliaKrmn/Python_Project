export class ShopPage {
    goToSpecificPage() {
      cy.visit('https://magento.softwaretestingboard.com/')
    }
  
    findElement(productName) {
      cy.get('input[name="q"]').type(productName + '{enter}')
    }
  
    validateResults(productName) {
      cy.contains(productName).should('exist')
    }
  
    searchForText(text) {
      cy.contains(text).should('be.visible')
    }
  
    addProductToCart(productName) {
      this.findElement(productName)
      cy.contains(productName).click()
      cy.get('#product-addtocart-button').click()
    }
  
    hoverAndAddToCart(productName) {
      this.findElement(productName)
      cy.contains(productName).trigger('mouseover')
      cy.contains('Add to Cart').click()
    }
  
    changeQuantity(qty) {
      cy.get('input.qty').clear().type(qty)
    }
  
    removeFromCart() {
      cy.get('.action-delete').click()
    }
  
    validateCartIsEmpty() {
      cy.contains('You have no items in your shopping cart.').should('be.visible')
    }
  }