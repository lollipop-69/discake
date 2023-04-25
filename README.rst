dpy-utils
==========

.. image:: https://discord.com/api/guilds/815886477066108968/embed.png
   :target: https://discord.gg/egvmz5NjSZ
   :alt: Discord server invite
.. image:: https://img.shields.io/pypi/v/discord.py.svg
   :target: https://pypi.python.org/pypi/discord.py
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/discord.py.svg
   :target: https://pypi.python.org/pypi/discord.py
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
    python3 -m pip install -U dpy-utils

    # Windows
    py -3 -m pip install -U dpy-utils


Quick Example
--------------

.. code:: py

    import discord
    from discord import Embed, Intents
    from discord.ext import commands
    from dpyutils import Paginator

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

- `Official Discord Server <https://discord.gg/egvmz5NjSZ>`_
