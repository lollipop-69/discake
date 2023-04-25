from __future__ import annotations

from typing import TYPE_CHECKING, Union, List, Any, Optional

from discord import Embed, ButtonStyle, Interaction
from discord.ui import View, Button
from discord.ext.commands import Context

if TYPE_CHECKING:
    from discord import Member, Message, InteractionMessage, WebhookMessage
    
__all__ = (
  'Paginator',
  'ButtonsView
)

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

    class PreviousButton(.Button):
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
            if isinstance(self.task._pages[self.task._index], discord.Embed):
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
    
    async def interaction_check(self, interaction:discord.Interaction):
        return True if interaction.user == self.task.author else await interaction.response.send_message('This is not for you', ephemeral=True)
      
class Paginator:
    """
    The Paginator class is used for paginating through a list of items, such as list of embeds.
    It allows for easy navigation between pages using the "previous" and "next" buttons.

    Attributes:
    entries (List[Any]): List of items to be paginated.
    timeout (Optional[float]): The timeout value of the View.
    first (str): The emoji for representing the button for the first page.
    previous (str): The emoji for representing the button for the preceding page.
    clear (str): The emoji for representing the button for disabling buttons.
    next (str): The emoji for representing the button for the succeeding page.
    last (str): The emoji for representing the button for the last page.

    Methods:
    send(obj: Union[Context, Interaction]): Starts the paginator and sends the message
    """    
    def __init__(
        self,
        *, 
        entries: List[Any] = None,
        timeout: Optional[float] = 180,
        first = '⏮',
        previous = '◀',
        clear = '⏹',
        next = '▶',
        last = '⏭',
        ephemeral: bool = False      
    )
    super().__init__()
    
    self.first = first
    self.prev = previous
    self.clear = clear
    self.next = next
    self.last = last

    self.author: Member = None
    self.page: Message = None
    self._pages = []
    self._index = 0
    self.ephemeral = ephemeral
    self.timeout = timeout
    self.entries: Any = entries
    
    async def send(self, interaction: Union[Context, Interaction]):
        if not self.entries:
            raise AttributeError('You must provide atleast one entry or page for pagination.') 
            
        self.author = interaction.user if isinstance(interaction, Interaction) else interaction.author
        entries = self.entries
        for chunk in entries:
            self._pages.append(chunk)
            
        view = ButtonsView(task = self, timeout = self.timeout, previous = self.prev, next = self.next, first = self.first,clear = self.clear, last = self.last)
        
        if isinstance(self._pages[0], Embed):
            if len(self._pages) > 1:
                if isinstance(interaction, Interaction):
                    self.page = await interaction.followup.send(embed=self._pages[0],view=view,ephemeral=self.ephemeral)
                else:
                    self.page = await interaction.send(embed=self._pages[0],view=view)
            else:
                if isinstance(interaction, Interaction):
                    self.page = await interaction.followup.send(embed=self._pages[0],ephemeral=self.ephemeral)
                else:
                    self.page = await interaction.send(embed=self._pages[0])
