from skills import Skills


class SkillFactory:

    @staticmethod
    def create_skills(skill_types):
        # Although player classes can start with these skills, they can be given to any enemy as well
        all_skills = {
            # Starting warrior skills
            'slash': Skills('Slash', 15, 4),
            'swing': Skills('Swing', 12, 3),
            'stab': Skills('Stab', 10, 2),

            # Starting Rogue skills
            'backstab': Skills('Backstab', 15, 2),
            'silent_strike': Skills('Silent Strike', 12, 1),
            'sap': Skills('Sap', 10, 0),

            # Starting Mage skills
            'fireball': Skills('Fireball', 20, 5),
            'flames': Skills('Flames', 15, 3),
            'magma': Skills('Magma', 12, 2),
            'blaze': Skills('Blaze', 17, 4),

            # Starting Commoner Skills
            'bash': Skills('Bash', 7, 1),
            'whack': Skills('Whack', 7, 1),

            # Basic Enemy skills
            'bite': Skills('Bite', 12, 1)
        }

        skills_to_return = []
        for skill_type in skill_types:
            if skill_type in all_skills:
                skills_to_return.append(all_skills[skill_type])
            else:
                raise ValueError(f'Unknown skill type: {skill_type}')

        return skills_to_return
