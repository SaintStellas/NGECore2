import sys

def setup(core, actor, buff):
	core.skillModService.addSkillMod(actor, 'expertise_glancing_blow_all', 60)
	
	return
	
def removeBuff(core, actor, buff):
	core.skillModService.deductSkillMod(actor, 'expertise_glancing_blow_all', 60)
	return