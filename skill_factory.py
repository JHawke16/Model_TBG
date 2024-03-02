from skills import Skills


class SkillFactory:

    @staticmethod
    def create_skills(skill_types):
        all_skills = {
            'slash': Skills('Slash', 15, 4),
            'swing': Skills('Swing', 12, 3),
            'stab': Skills('Stab', 10, 2),
            'bite': Skills('Bite', 7, 1)
        }

        skills_to_return = []
        for skill_type in skill_types:
            if skill_type in all_skills:
                skills_to_return.append(all_skills[skill_type])
            else:
                raise ValueError(f'Unknown skill type: {skill_type}')

        return skills_to_return

