Feature: Tide

  Scenario: SignUp to website
    Given launch chrome browser
    When I open Tide Homepage
    When Click On Register
    When Click On Sign Up Now
    When Enter firstname "Rohit" and email "rohitbhagat7865@gmail.com" and password"admin123"
    When Click on create account
    And User must Thanks for signing up!


  Scenario: SignUp to website
    Given Click On Register
    When click on Log in
    When Enter "Username and Password
    And Click on Log in

  Scenario: Search the product

    Given Click on search box
    When Enter Product Name
    When Click on search Box
    When Click on the Product
    And click on the retailers

  Scenario:search the product
    Given Click on search box
    When Enter Product Name
    When Click on search box
    When Click on Product
    And Click on retailers

  Scenario: What's new
    Given Click on Whats new
    When Click on product
    When Click on retailers
    And back to home page

  Scenario: Go How to Wash cloth
    Given Click on how to wash cloth
    When Click on how to remove stains

  Scenario:Go to Our Commitment
    Given Click on Our Commitment
    When Click on Our ambition
    And Go to home page

  Scenario: Go to Contact Us
    Given Click on Contact Us
    When Click on Type here for answer and ask question
    And Click on search box

