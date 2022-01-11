 describe('Visit Website', () => {
    it('UKTV Play', () => {
      cy.visit('https://uktvplay.uktv.co.uk')
// Sign in to website.
cy.wait(4000)
    cy.contains('Yes').click()
    cy.contains('Account').click()
    cy.get('form').within(() => {
    cy.get('#email').type("marc.jackson@uktv.co.uk") // Only yield inputs within form
    cy.get('#password').type("Batman47") // Only yield textareas within form
})

   cy.get('#sign-in-btn').click()
   cy.wait(4000)

   // Navigation for Categories 
   cy.get('#nav-bar-categories').click().get('#nav-bar-drama').click()
   cy.wait(2000)
   cy.get('#nav-bar-categories').click().get('#nav-bar-comedy').click()
   cy.wait(2000)
   cy.get('#nav-bar-categories').click().get('#nav-bar-entertainment').click()
   cy.wait(2000)
   cy.get('#nav-bar-categories').click().get('#nav-bar-soaps').click()
   cy.wait(2000)
   cy.get('#nav-bar-categories').click().get('#nav-bar-documentaries').click()
   cy.wait(3000)

   // Navigation for Boxsets
   cy.get('#nav-bar-boxsets').click()
   cy.get('#tab-collections > span').click()
   cy.wait(3000)

   //Navigation for A-Z
   cy.get('#nav-bar-az').click()
   cy.wait(3000)
   cy.get('#subs-on').click()
   cy.wait(3000)

   //Navigation to More Page and Tabs
   cy.get('#nav-bar-more').click()
   cy.wait(1000)
   cy.get('#tab-ways-to-watch > span').click()
   cy.wait(4000)
   cy.get('#tab-parental-controls > span').click()
   cy.wait(4000)
   cy.get('#tab-accessibility > span').click()
   cy.wait(4000)
   cy.get('#tab-help > span').click()
   cy.wait(4000)
   cy.get('#tab-contact > span').click()
   cy.wait(4000)
   
    //cy.get('form').within(() => {
    //cy.get('<input data-v-5f809c52="" placeholder="First name" name="firstName" maxlength="30" required="required" id="vf8606620281" vue-form-validator="" class="vf-pristine vf-invalid vf-touched vf-invalid-required">').type("Melvin") // Only yield inputs within form
    //cy.get('#vfh6o10w4ekg').type("Winters") // Only yield textareas within form
    //cy.get('#vfmi0oyeyy9q').type("marc.jackson@uktv.co.uk")
    //cy.get('#vfw51t737yng').type("have a nice day")
//}



   //Sign Out
   cy.get('#nav-bar-account > div > span > img').click()
   cy.get('#sign-out').click()

     })

    })