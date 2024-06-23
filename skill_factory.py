from skills import Skills


class SkillFactory:

    @staticmethod
    def create_skills(skill_types, rarity):
        all_skills = {
            'basic': {
                'slash': Skills('Slash', 15, 4, ['sword', 'dagger']),
                'swing': Skills('Swing', 13, 3, ['sword', 'club']),
                'stab': Skills('Stab', 12, 2, ['sword', 'dagger']),
                'backstab': Skills('Backstab', 15, 2, ['dagger']),
                'silent_strike': Skills('Silent Strike', 12, 1, ['dagger']),
                'sap': Skills('Sap', 10, 0, ['dagger']),
                'fireball': Skills('Fireball', 20, 5, ['staff']),
                'flames': Skills('Flames', 15, 3, ['staff']),
                'magma': Skills('Magma', 12, 2, ['staff']),
                'blaze': Skills('Blaze', 17, 4, ['staff']),
                'bash': Skills('Bash', 7, 1, ['club']),
                'whack': Skills('Whack', 7, 1, ['club']),
                'bite': Skills('Bite', 12, 1, ['claw'])
            },
            'rare': {
                'slash': Skills('Power Slash', 25, 6, ['sword', 'dagger']),
                'swing': Skills('Heavy Swing', 20, 5, ['sword', 'club']),
                'stab': Skills('Deep Stab', 18, 4, ['sword', 'dagger']),
                'fireball': Skills('Inferno Fireball', 30, 7, ['staff']),
                'blaze': Skills('Firestorm', 25, 6, ['staff'])
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

