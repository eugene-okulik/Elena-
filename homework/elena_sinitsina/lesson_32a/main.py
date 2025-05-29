import datetime

motivations = {
    0: "🌞 Monday: A fresh start. Make it count!",
    1: "💡 Tuesday: Progress over perfection.",
    2: "💥 Wednesday: You're halfway there!",
    3: "🌈 Thursday: Small steps = Big results.",
    4: "🔥 Friday: Finish strong!",
    5: "😎 Saturday: Recharge and reflect.",
    6: "🎯 Sunday: Plan, dream, believe."
}

today = datetime.datetime.today().weekday()
print("💬 Your motivation for today:")
print(motivations[today])