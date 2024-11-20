from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    
   
    self.gefaengnisse_drop_down.items = [{'text': name, 'value': id} for name, id in anvil.server.call('get_gefaengnisse')]
    

    self.gefaengnisse_drop_down.selected_value = 1  
    self.update_gefaengnis_details(1)

  def update_gefaengnis_details(self, gefaengnis_id):
    """Update form details based on the selected prison"""
    if gefaengnis_id == 1:  
      self.label_direktor.text = "Dr. Schmidt"
      self.label_freie_zellen.text = "Freie Zellen: 15"
      self.repeating_zellen.items = [
          {'zellennummer': '101', '1': 'TODO'},
          {'zellennummer': '102', '2': 'TODO'},
          {'zellennummer': '103', '1': 'TODO'}
      ]
    elif gefaengnis_id == 2:  # Gefängnis Süd
      self.label_direktor.text = "Dr. Meyer"
      self.label_freie_zellen.text = "Freie Zellen: 18"
      self.repeating_zellen.items = [
          {'zellennummer': '201', '1': 'TODO'},
          {'zellennummer': '202', '0': 'TODO'}
      ]

  def gefaengnisse_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    selected_value = self.gefaengnisse_drop_down.selected_value
    self.update_gefaengnis_details(selected_value)



  
 
