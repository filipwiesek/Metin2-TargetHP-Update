## find:
		hpGauge = ui.Gauge()
		hpGauge.SetParent(self)
		hpGauge.MakeGauge(130, "red")
		hpGauge.Hide()

## paste below:
		hpText = ui.TextLine()
		hpText.SetParent(hpGauge)
		hpText.SetPosition(0, -15)
		hpText.SetWindowHorizontalAlignCenter()
		hpText.SetHorizontalAlignCenter()
		hpText.SetOutline(True)
		hpText.Hide()

## find:
		self.hpGauge = hpGauge

## paste below:
		self.hpText = hpText

## find:
		self.hpGauge = None

## paste below:
		self.hpText = None

## find:
		self.hpGauge.Show()

## paste below:
		self.hpText.Show()

## find:
	def SetHP(self, hpPercentage):
		[...]

## replace with:
	def SetHP(self, hpNow, hpMax):
		if not self.hpGauge.IsShow():

			self.SetSize(200 + 7 * self.nameLength, self.GetHeight())
			self.name.SetPosition(23, 13)
			self.name.SetWindowHorizontalAlignLeft()
			self.name.SetHorizontalAlignLeft()

			self.hpGauge.Show()
			self.hpText.Show()
			self.UpdatePosition()

		'''
		if app.ENABLE_POISON_GAUGE_EFFECT:
			if chrmgr.HasAffectByVID(self.GetTargetVID(), chr.AFFECT_POISON):
				self.hpGauge.SetGaugeColor("lime")
			else:
				self.hpGauge.SetGaugeColor("red")
		'''

		self.hpGauge.SetPercentage(hpNow, hpMax)

		self.hpText.SetText("%s/%s (%.2f%%)" 
							% (localeInfo.NumberToMoneyString(hpNow)[:-5],
							   localeInfo.NumberToMoneyString(hpMax)[:-5],
							   max(0, (float(hpNow) / max(1, float(hpMax)) * 100))))