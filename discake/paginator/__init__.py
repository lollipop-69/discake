from __future__ import annotations

from typing import TYPE_CHECKING, Union, List, Any, Optional

from discord import Embed, ButtonStyle, Interaction
from discord.ui import View, Button
from discord.ext.commands import Context

from .utils.paginate import ButtonsView

if TYPE_CHECKING:
    from discord import Member, Message, InteractionMessage, WebhookMessage
    
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
    first (str): The emoji for representing the button for the first page.
    previous (str): The emoji for representing the button for the preceding page.
    clear (str): The emoji for representing the button for disabling buttons.
    next (str): The emoji for representing the button for the succeeding page.
    last (str): The emoji for representing the button for the last page.
    ephemeral (bool): Sends an ephemeral message if True. (while using this class in a slash command)

    Methods:
    send(interaction: Union[Context, Interaction]): Starts the paginator and sends the message
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
        elif isinstance(self._pages[0], str):
            if len(self._pages) > 1:
                if isinstance(interaction, Interaction):
                    self.page = await interaction.followup.send(content=self._pages[0],view=view,ephemeral=self.ephemeral)
                else:
                    self.page = await interaction.send(content=self._pages[0],view=view)
            else:
                if isinstance(interaction, Interaction):
                    self.page = await interaction.followup.send(content=self._pages[0],ephemeral=self.ephemeral)
                else:
                    self.page = await interaction.send(content=self._pages[0])
        else:
            raise TypeError("Entries should be of type 'discord.Embed' or 'string'")
