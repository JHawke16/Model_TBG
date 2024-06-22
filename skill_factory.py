from skills import Skills


class SkillFactory:

    @staticmethod
    def create_skills(skill_types, rarity):
        all_skills = {
            'basic': {
                'slash': Skills('Slash', 15, 4),
                'swing': Skills('Swing', 13, 3),
                'stab': Skills('Stab', 12, 2),
                'backstab': Skills('Backstab', 15, 2),
                'silent_strike': Skills('Silent Strike', 12, 1),
                'sap': Skills('Sap', 10, 0),
                'fireball': Skills('Fireball', 20, 5),
                'flames': Skills('Flames', 15, 3),
                'magma': Skills('Magma', 12, 2),
                'blaze': Skills('Blaze', 17, 4),
                'bash': Skills('Bash', 7, 1),
                'whack': Skills('Whack', 7, 1),
                'bite': Skills('Bite', 12, 1)
            },
            'rare': {
                'slash': Skills('Power Slash', 25, 6),
                'swing': Skills('Heavy Swing', 20, 5),
                'stab': Skills('Deep Stab', 18, 4),
                'fireball': Skills('Inferno Fireball', 30, 7),
                'blaze': Skills('Firestorm', 25, 6)
            }
            # Add more rarities as needed
        }

        skills_to_return = []
        for skill_type in skill_types:
            if rarity in all_skills and skill_type in all_skills[rarity]:
                skills_to_return.append(all_skills[rarity][skill_type])
            else:
                raise ValueError(f'Unknown skill type or rarity: {skill_type}, {rarity}')

        return skills_to_return
