# Created by matifonseca at 02/02/2022
Feature: Como usuario de la sdk quiero crear un track

  Scenario: Creacion exitosa
    Given que quiero trackear para el path "/home" y si el usuario esta logeado
    When creo el track
    Then se me informa que se creo correctamente

  Scenario: Error en la creacion
    Given que quiero trackear para el path "/home" y si el usuario esta logeado
    When creo el track
    And ocurre un error al enviarlo
    Then se me informa que no se pudo enviar el track