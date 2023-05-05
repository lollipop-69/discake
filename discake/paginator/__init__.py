from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union, List, Any, Optional

from discord import Embed, Interaction
from discord.ext.commands import Context

from discake.utils import ButtonsView

if TYPE_CHECKING:
    from discord import Member, Message
    
__all__ = (
  'Paginator'
)
      
class Paginator:
    """
    The Paginator class is used for paginating through a list of items, such as list of embeds.
    It allows for easy navigation between pages using the "previous" and "next" buttons.

    Attributes:
    entries (List[Any]): List of items to be paginated.
    timeout (Optional[float]): The timeout value of the View.
    color (Literal['blurple', 'grey', 'green','red']): The color of the buttons.
    first (str): The emoji for representing the button for the first page.
    previous (str): The emoji for representing the button for the preceding page.
    clear (str): The emoji for representing the button for disabling buttons.
    next (str): The emoji for representing the button for the succeeding page.
    last (str): The emoji for representing the button for the last page.

    Methods:
    send(interaction: Union[Context, Interaction]): Starts the paginator and sends the message.
    """    
    def __init__(
        self,
        *, 
        entries: List[Any] = None,
        timeout: Optional[float] = 180,
        color: Literal['blurple', 'grey', 'green', 'red'] = 'grey',
        first = '⏮',
        previous = '◀',
        clear = '⏹',
        next = '▶',
        last = '⏭'     
    ):
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
        self.timeout = timeout
        self.color = color
        self.entries: Any = entries
    
    async def send(self, interaction: Union[Context, Interaction]):
        """
        Sends or starts the paginator

        Attributes:
        interaction (Union[Context, Interaction): The Interaction or Context to respond to.
        """
        if not self.entries:
            raise AttributeError('You must provide atleast one entry or page for pagination.') 
            
        self.author = interaction.user if isinstance(interaction, Interaction) else interaction.author
        entries = self.entries
        for chunk in entries:
            self._pages.append(chunk)
            
        view = ButtonsView(task = self, color = self.color, timeout = self.timeout, previous = self.prev, next = self.next, first = self.first,clear = self.clear, last = self.last)
        
        if isinstance(self._pages[0], Embed):
            if len(self._pages) > 1:
                if isinstance(interaction, Interaction):
                    self.page = await interaction.followup.send(embed=self._pages[0],view=view) 
                else:
                    self.page = await interaction.send(embed=self._pages[0],view=view)
            else:
                if isinstance(interaction, Interaction):
                    self.page = await interaction.response.send_message(embed=self._pages[0])
                else:
                    self.page = await interaction.send(embed=self._pages[0])
        elif isinstance(self._pages[0], Union[str, int]):
            if len(self._pages) > 1:
                if isinstance(interaction, Interaction):
                    self.page = await interaction.followup.send(content=self._pages[0],view=view)
                else:
                    self.page = await interaction.send(content=self._pages[0],view=view)
            else:
                if isinstance(interaction, Interaction):
                    self.page = await interaction.response.send_message(content=self._pages[0])
                else:
                    self.page = await interaction.send(content=self._pages[0])
        else:
            raise TypeError("Entries should be of type 'discord.Embed' or 'string'")
