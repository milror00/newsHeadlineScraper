# Created by Oem at 21/04/2020
Feature: To capture the TOP headline and image.

  Scenario: Get the headline for a given newspaper

    Given I am I have a list of newspaper urls
      |url                         |newspaper    |
      |https://foxnews.com         |foxnews      |

    And I capture the top headline for each newspaper
    Then for each headline I can write it out to stdout