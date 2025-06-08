import { ShopPage } from '../support/pages/ShopPage'

describe('Shop Page Tests', () => {
  it('should search and find an existing product', () => {
    const shop = new ShopPage()
    shop.goToSpecificPage()
    shop.findElement('Olivia')
    shop.validateResults('Olivia')
  })

  it('should show empty result for non-existing product', () => {
    const shop = new ShopPage()
    shop.goToSpecificPage()
    shop.findElement('Jerusalem')
    shop.searchForText('Your search returned no results.')
  })

  it('should add product to cart', () => {
    const shop = new ShopPage()
    shop.goToSpecificPage()
    shop.addProductToCart('Atlas')
  })

  it('should add item via hover', () => {
    const shop = new ShopPage()
    shop.goToSpecificPage()
    shop.hoverAndAddToCart('Atlas')
  })

  it('should change quantity in cart', () => {
    const shop = new ShopPage()
    shop.changeQuantity('10')
  })

  it('should remove product and validate empty cart', () => {
    const shop = new ShopPage()
    shop.removeFromCart()
    shop.validateCartIsEmpty()
  })
})