import sys

def setup(core, actor, buff):
	core.skillModService.addSkillMod(actor, 'critical_hit_vulnerable', 6)
	
	return
	
def removeBuff(core, actor, buff):
	core.skillModService.deductSkillMod(actor, 'critical_hit_vulnerable', 6)
	return