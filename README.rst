discake
==========

.. image:: https://discord.com/api/guilds/815886477066108968/embed.png
   :target: https://discord.gg/egvmz5NjSZ
   :alt: Discord server invite
.. image:: https://img.shields.io/pypi/v/discake.svg
   :target: https://pypi.python.org/pypi/discake
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/discake.svg
   :target: https://pypi.python.org/pypi/discake
   :alt: PyPI supported Python versions

A discord py util library.

Key Features
-------------

- Button Paginator

Installing
----------

**Python 3.8 or higher is required**


.. code:: sh

    # Linux/macOS
    python3 -m pip install -U discake

    # Windows
    py -3 -m pip install -U discake


Quick Example
--------------

.. code:: py

    import discord
    from discord import Embed, Intents
    from discord.ext import commands
    from discake import Paginator

    class MyBot(comamnds.Bot):
        def __init__(self):
            super().__init__(command_prefix = '!')
            
        async def on_ready(self):
            print('Logged on as', self.user)

    client = MyBot(intents=Intents.default())
    
    @client.command(name = 'paginate', description = 'Pagination using the library')
    async def _paginate(ctx):
        entry_list = []
        for i in range(0,20):
            embed = Embed(description = f'This is the {i}th page')
            entry_list.append(embed)
        paginate_object = Paginator(
                entries = entry_list,
                timeout = 10.0
        )
        await paginate_object.send(ctx)
    
    
    client.run('TOKEN')

Links
------

.. image:: https://invidget.switchblade.xyz/egvmz5NjSZ?theme=light
   :target: https://discord.gg/egvmz5NjSZ
   :alt: Support Server

Author
------
.. image:: https://discord.c99.nl/widget/theme-3/545953035776688139.png
   :target: https://discord.gg/egvmz5NjSZ
   :alt: Author Info