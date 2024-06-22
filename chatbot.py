import openai

openai.api_key = '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'

def train_chatbot(training_text):
    messages = [
        {"role": "system", "content": training_text}
    ]
    return messages

def chat_with_bot(messages, user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    reply = response['choices'][0]['message']['content'].strip()
    messages.append({"role": "assistant", "content": reply})
    return reply

#Training text
training_text = """
STDs are infections that are passed from one person to another during sexual activity. Anybody who has oral sex, anal sex, vaginal sex, genital skin-to-skin contact, or who shares sexual fluids with another person can get STDs. Safer sex (often called “safe sex”) means taking steps to protect yourself and your partner from STDs when you have sex.

There are lots of ways you can make sex safer. One of the best ways is by using a barrier — like condoms, internal condoms, dental dams, and/or latex or nitrile gloves — every single time you have oral, anal, or vaginal sex, or do anything that can pass sexual fluids (like sharing sex toys). Barriers protect you and your partner from sexual fluids and some skin-to-skin contact, which can both spread STDs.  

Getting tested for STDs regularly is also part of safer sex, even if you always use barriers like condoms and feel totally fine. Most people with STDs don’t have symptoms or know they’re infected, and they can easily pass the infection to their partners. So testing is the only way to know for sure whether or not someone has an STD.

Getting tested also protects you by letting you know if you DO have an STD, so you can get the right treatment to stay healthy and avoid giving it to other people.

Sticking to sexual activities that don’t spread STDs — like outercourse or mutual masturbation (masturbating while with each other) — is a great way to safely get sexual pleasure and be intimate with another person. But if you’re taking off underwear and touching each other, sharing sexual fluids, or having any kind of sex, using barriers is the safer way to go.

If you touch your partner’s genitals with your hands, wash your hands before touching your own genitals, mouth, or eyes to avoid passing sexual fluids. If you’re sharing sex toys, make sure to wash the toys with soap and water before they touch another person’s body. You can also use condoms on sex toys — change the condom before it touches another person’s body.

Another way to make sex safer is to avoid drinking too much alcohol or doing other drugs. Getting wasted can make you forget how important safer sex is, and you may accidentally make decisions that increase your chances of getting STDs. It’s also harder to use condoms correctly and remember other safer sex basics when you’re drunk or high.

The only way to be totally sure you won’t get an STD is to never have any kind of sexual contact with another person. But that doesn’t work for the vast majority of people — most of us are sexually intimate with other people at some point in our lives. So if you’re going to have sex, making it safer sex is the best way to help you avoid getting or passing an STD.

How do you get STDs?
STDs are usually passed from one person to another during oral, anal, or vaginal sex. There are lots of different STDs. Some are carried in body fluids like semen (cum), vaginal fluids, and blood. Others can be passed just from skin-to-skin touching with an infected body area. Using barriers like condoms and dams helps you avoid contact with fluids and some types of skin-to-skin contact during sex. So when you don’t use condoms, your chance of getting an STD goes up.

All STDs can infect your genitals. Vaginal or anal sex without a condom can spread:

chlamydia

gonorrhea

syphilis

HIV

herpes

HPV and genital warts

hepatitis B

pubic lice

scabies

trichomoniasis

Some STDs can also infect your lips, mouth, and throat. Oral sex without a condom or dam can spread:

herpes

syphilis

gonorrhea

chlamydia

HPV

hepatitis B

Some STDs can be passed even if there’s only some skin-on-skin action with no fluids passed. Genital skin-to-skin contact can spread:

herpes

HPV and genital warts

syphilis

pubic lice

scabies

molluscum contagiosum

Keep in mind that any activity that passes sexual fluids (like sharing sex toys, or touching each other’s genitals when there are sexual fluids on your hand), may also spread some STDs, like chlamydia and gonorrhea. Using barriers like condoms, dental dams, and latex or nitrile gloves can help lower contact with sexual fluids and help prevent spreading STDs.

Are some kinds of sex safer than others?
Yup. There are even a few totally risk-free ways to get sexual pleasure and be intimate with another person, like masturbating, dry humping (aka grinding) with clothes on, and touching your partner’s genitals with your hands (as long as you don’t get any of their sexual fluids on or in your mouth or genitals).

Lower risk activities include kissing, using sex toys with a partner, dry humping (grinding) without clothes, and oral sex . But it’s still possible to get certain STDs from these things, so using condoms and dams to avoid contact with skin and fluids whenever you can helps you stay healthy.

Having vaginal or anal sex without a condom is super risky. You can get any and all STDs from unprotected vaginal or anal sex. The best way to protect yourself if you’re going to have vaginal or anal sex is use a condom every single time. Using lube with that condom also makes sex safer, especially anal sex.

When it comes to HIV, oral sex is much safer sex than vaginal or anal sex. But other infections, like herpes, syphilis, hepatitis B, gonorrhea, and HPV, can be passed during oral sex. So no matter what kind of sex you have, use condoms or dams to make it safer.

If I have an STD, how can I have safer sex?
If you find out that you have an STD, it’s important to know how to have safer sex and avoid passing it on. Luckily, many STDs can be easily cured with medication, so once you finish treatment, you don’t have to worry about giving your STD to anyone.

And even though some STDs can’t be cured, there are ways to treat your symptoms and help avoid giving your STD to people you have sex with. Depending on what STD you have, there are things you can do to protect your partners. Here’s a handy checklist:

Always use condoms and dental dams during oral, anal, and vaginal sex — whether or not you have an STD.

Don’t have sexual contact at all if you have any STD symptoms (like sores or warts around your genitals, weird discharge from your penis, vagina or anus, or itching, pain, irritation and/or swelling in your penis, vagina, vulva, or anus).

Go see a doctor or nurse so they can start treating your STD as soon as possible.

If you have a curable STD (like gonorrhea, chlamydia, or syphilis), take all of your medication the way your doctor tells you to, even if your symptoms go away sooner. The infection stays in your body until you totally finish the treatment. Your partner(s) should also be treated at the same time. Don’t have sex at all until you both finish your treatment, and your doctor or nurse says it’s OK.

If you have an STD that can’t be cured (like HIV or herpes), talk with your doctor about medicines that can help lower your chances of spreading it to a partner. Depending on what STD you have and where it is, you may need to use condoms/dams every time you have oral, anal, and/or vaginal sex.

Limit your sexual activity to only one partner who is having sex only with you to reduce exposure to disease-causing organisms. Follow these guidelines, which may provide for safer sex:

Think twice before beginning sexual relations with a new partner. First, discuss past partners, history of STIs, and drug use.

Use condoms every time you have sex. Choose a male condom made of latex or polyurethane--not natural materials. Only use polyurethane if you are allergic to latex. Female condoms are made of polyurethane.

Although studies say that nonoxynol-9 spermicide kills HIV in lab testing, it has not been determined whether spermicides, used alone or with condoms, provide protection against HIV. There are data that shows nonoynol-9 may increase the risk of HIV transmission, However, the CDC recommends that latex condoms, with or without spermicides, should be used to help prevent sexual transmission of HIV.

For oral sex, help protect your mouth by having your partner use a condom (male or female).

Avoid drinking alcohol or using drugs as this increases the chance that you will participate in high-risk sex.

Women should not douche after intercourse--it does not protect against STIs. And, it could spread an infection farther into the reproductive tract, and can wash away spermicidal protection.

Have regular Pap tests, pelvic exams, and periodic tests for STIs.

Be aware of your partner's body. Look for signs of a sore, blister, rash, or discharge.

Check your body frequently for signs of a sore, blister, rash, or discharge.

Consider sexual activities other than vaginal, oral, or anal sex. These are techniques that do not involve the exchange of body fluids or contact between mucous membranes.
"""

messages = train_chatbot(training_text)

print("Welcome to the chatbot! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    bot_response = chat_with_bot(messages, user_input)
    print(f"Bot: {bot_response}")
    