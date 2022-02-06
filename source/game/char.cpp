// find:
	p.header = HEADER_GC_TARGET;
	p.dwVID = 0;
	p.bHPPercent = 0;

// replace with:
	p.header = HEADER_GC_TARGET;
	p.dwVID = 0;
	p.dwHp = 0;
	p.dwHpMax = 0;

// find:
	if (m_pkChrTarget)
	{
		m_pkChrTarget->m_set_pkChrTargetedBy.insert(this);

		p.dwVID	= m_pkChrTarget->GetVID();

		if (m_pkChrTarget->IsPC() && !m_pkChrTarget->IsPolymorphed() || m_pkChrTarget->GetMaxHP() <= 0)
			p.bHPPercent = 0;
		else 
		{
			if (m_pkChrTarget->GetRaceNum() == 20101 ||
					m_pkChrTarget->GetRaceNum() == 20102 ||
					m_pkChrTarget->GetRaceNum() == 20103 ||
					m_pkChrTarget->GetRaceNum() == 20104 ||
					m_pkChrTarget->GetRaceNum() == 20105 ||
					m_pkChrTarget->GetRaceNum() == 20106 ||
					m_pkChrTarget->GetRaceNum() == 20107 ||
					m_pkChrTarget->GetRaceNum() == 20108 ||
					m_pkChrTarget->GetRaceNum() == 20109)
			{
				LPCHARACTER owner = m_pkChrTarget->GetVictim();

				if (owner)
				{
					int iHorseHealth = owner->GetHorseHealth();
					int iHorseMaxHealth = owner->GetHorseMaxHealth();

					if (iHorseMaxHealth)
						p.bHPPercent = MINMAX(0,  iHorseHealth * 100 / iHorseMaxHealth, 100);
					else
						p.bHPPercent = 100;
				}
				else
					p.bHPPercent = 100;
			}
			else
				p.bHPPercent = MINMAX(0, (m_pkChrTarget->GetHP() * 100) / m_pkChrTarget->GetMaxHP(), 100);
		}
	}
	else
	{
		p.dwVID = 0;
		p.bHPPercent = 0;
	}

// replace with:
	if (m_pkChrTarget)
	{
		m_pkChrTarget->m_set_pkChrTargetedBy.insert(this);

		p.dwVID	= m_pkChrTarget->GetVID();

		if (m_pkChrTarget->IsPC() && !m_pkChrTarget->IsPolymorphed() || m_pkChrTarget->GetMaxHP() <= 0)
		{
			p.dwHp = 0;
			p.dwHpMax = 0;
		}
		else 
		{
			if (m_pkChrTarget->GetRaceNum() == 20101 ||
					m_pkChrTarget->GetRaceNum() == 20102 ||
					m_pkChrTarget->GetRaceNum() == 20103 ||
					m_pkChrTarget->GetRaceNum() == 20104 ||
					m_pkChrTarget->GetRaceNum() == 20105 ||
					m_pkChrTarget->GetRaceNum() == 20106 ||
					m_pkChrTarget->GetRaceNum() == 20107 ||
					m_pkChrTarget->GetRaceNum() == 20108 ||
					m_pkChrTarget->GetRaceNum() == 20109)
			{
				LPCHARACTER owner = m_pkChrTarget->GetVictim();

				if (owner)
				{
					int iHorseHealth = owner->GetHorseHealth();
					int iHorseMaxHealth = owner->GetHorseMaxHealth();

					if (iHorseMaxHealth)
					{
						p.dwHp = iHorseHealth;
						p.dwHpMax = iHorseMaxHealth;
					}
					else
					{
						p.dwHp = 100;
						p.dwHpMax = 100;
					}
				}
				else
				{
					p.dwHp = 100;
					p.dwHpMax = 100;
				}
			}
			else
			{
				p.dwHp = m_pkChrTarget->GetHP();
				p.dwHpMax = m_pkChrTarget->GetMaxHP();
			}
		}
	}
	else
	{
		p.dwVID = 0;
		p.dwHp = 0;
		p.dwHpMax = 0;
	}

// find:
	if (IsPC())
		p.bHPPercent = 0;
	else
		p.bHPPercent = MINMAX(0, (GetHP() * 100) / GetMaxHP(), 100);

// replace with:
	if (IsPC())
	{
		p.dwHp = 0;
		p.dwHpMax = 0;
	}
	else
	{
		p.dwHp = GetHP();
		p.dwHpMax = GetMaxHP();
	}