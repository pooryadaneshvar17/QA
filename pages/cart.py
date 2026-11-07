from playwright.sync_api import Page ,expect


class Cart():

    def __init__(self,page:Page):

        self.backpack=page.get_by_text("Sauce Labs Backpack")

        self.bike_light=page.get_by_text("Sauce Labs Bike Light")

        self.t_shirt=page.get_by_text("Sauce Labs Bolt T-Shirt",exact=True)


        self.check=page.locator("#checkout")






    def ok_item(self):

      expect(self.backpack).to_be_visible()
      expect(self.bike_light).to_be_visible()
      expect(self.t_shirt).to_be_visible()


      expect(self.backpack).to_contain_text("Sauce Labs Backpack")
      expect(self.bike_light).to_contain_text("Sauce Labs Bike Light")
      expect(self.t_shirt).to_contain_text("Sauce Labs Bolt T-Shirt")  


      


        
        