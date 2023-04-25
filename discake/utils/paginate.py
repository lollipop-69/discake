from __future__ import annnotations

from discord import Embed, ButtonStyle, Interaction
from discord.ui import View, Button

class ButtonsView(View):
    def __init__(
        self,
        task,
        timeout,
        first,
        previous,
        clear,
        next,
        last
    ):
        super().__init__(timeout=timeout)
        self.task = task
        self.previous = task._index
        self.add_item(self.FirstButton(task = task, emoji = first))
        self.add_item(self.PreviousButton(task = task, emoji = previous))
        self.add_item(self.ClearButton(task = task, emoji = clear))
        self.add_item(self.NextButton(task = task, emoji = next))
        self.add_item(self.LastButton(task = task, emoji = last))

    class FirstButton(Button):
        def __init__(self, task, emoji = None):
            super().__init__(style = ButtonStyle.primary, custom_id = 'first',emoji = emoji)
            self.task = task
        
        async def callback(self, interaction: Interaction):
            self.task._index = 0
            if isinstance(self.task._pages[self.task._index], Embed):
                await interaction.response.edit_message(embed=self.task._pages[self.task._index])
            else:
                await interaction.response.edit_message(content=self.task._pages[self.task._index]) 

    class PreviousButton(Button):
        def __init__(self, task, emoji = None):
            super().__init__(style = ButtonStyle.primary, custom_id = 'prev',emoji = emoji)
            self.task = task

        async def callback(self,interaction: Interaction):
            self.task._index += -1
            if self.task._index < 0:
                self.task._index = len(self.task._pages) - 1 
            if isinstance(self.task._pages[self.task._index], Embed):
                await interaction.response.edit_message(embed=self.task._pages[self.task._index])
            else:
                await interaction.response.edit_message(content=self.task._pages[self.task._index])  

    class ClearButton(Button):
        def __init__(self, task,  emoji = None):
            super().__init__(style = ButtonStyle.primary, custom_id = 'clear',emoji = emoji)
            self.task = task

        async def callback(self, interaction: Interaction):
            for i in self.view.children:
                i.disabled = True
            await interaction.response.edit_message(view=self.view)            

    class NextButton(Button):
        def __init__(self, task, emoji = None):
            super().__init__(style = ButtonStyle.primary, custom_id = 'next',emoji = emoji)
            self.task = task

        async def callback(self,interaction: Interaction):
            self.task._index += 1
            if self.task._index > len(self.task._pages) - 1 :
                self.task._index = 0 
            if isinstance(self.task._pages[self.task._index], Embed):
                await interaction.response.edit_message(embed=self.task._pages[self.task._index])
            else:
                await interaction.response.edit_message(content=self.task._pages[self.task._index]) 

    class LastButton(Button):
        def __init__(self, task, emoji = None):
            super().__init__(style = ButtonStyle.primary, custom_id = 'last',emoji = emoji)
            self.task = task

        async def callback(self,interaction: Interaction):
            self.task._index = len(self.task._pages) - 1
            if isinstance(self.task._pages[self.task._index], Embed):
                await interaction.response.edit_message(embed=self.task._pages[self.task._index])
            else:
                await interaction.response.edit_message(content=self.task._pages[self.task._index]) 

    async def on_timeout(self):
        for i in self.children:
            i.disabled = True
        await self.task.page.edit(view=self)
    
    async def interaction_check(self, interaction: Interaction):
        return True if interaction.user == self.task.author else await interaction.response.send_message('This is not for you', ephemeral=True)
