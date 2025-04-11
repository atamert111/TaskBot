# bot.py

import discord
from discord.ext import commands
from database import init_db, add_task, delete_task, show_tasks, complete_task

# Gerekli yetkilerle birlikte bot nesnesini oluştur
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Bot hazır olduğunda veritabanını başlat
@bot.event
async def on_ready():
    print(f'Bot çalışıyor: {bot.user}')
    init_db()

# !add_task <açıklama>
@bot.command(name="add_task")
async def add_task_cmd(ctx, *, description):
    add_task(description)
    await ctx.send(f"📌 Görev eklendi: {description}")

# !delete_task <id>
@bot.command(name="delete_task")
async def delete_task_cmd(ctx, task_id: int):
    delete_task(task_id)
    await ctx.send(f"🗑️ Görev silindi: {task_id}")

# !show_tasks → görev listesini göster
@bot.command(name="show_tasks")
async def show_tasks_cmd(ctx):
    tasks = show_tasks()
    
    if not tasks:
        await ctx.send("🚫 Hiç görev yok.")
        return

    message = "**📋 Görev Listesi:**\n"
    for task in tasks:
        status = "✅" if task[2] else "❌"
        message += f"{task[0]} - {task[1]} [{status}]\n"
    
    await ctx.send(message)

# !complete_task <id> → görevi tamamlandı olarak işaretle
@bot.command(name="complete_task")
async def complete_task_cmd(ctx, task_id: int):
    complete_task(task_id)
    await ctx.send(f"✔️ Görev tamamlandı: {task_id}")

# Botu başlat (TOKEN GİZLENDİ)
bot.run("DISCORD_BOT_TOKEN")
