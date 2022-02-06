## this part is optional for dynamic gauge bar

## find:
class Gauge(Window):
	[...]

## replace with:
class Gauge(Window):

	SLOT_WIDTH = 16
	SLOT_HEIGHT = 7

	GAUGE_TEMPORARY_PLACE = 12
	GAUGE_WIDTH = 16

	def __init__(self):
		Window.__init__(self)
		self.__oldValue = 0
		self.__newValue = 0
		self.width = 0

	def __del__(self):
		Window.__del__(self)

	def MakeGauge(self, width, color):

		self.width = max(48, width)

		imgSlotLeft = ImageBox()
		imgSlotLeft.SetParent(self)
		imgSlotLeft.LoadImage("d:/ymir work/ui/pattern/gauge_slot_left.tga")
		imgSlotLeft.Show()

		imgSlotRight = ImageBox()
		imgSlotRight.SetParent(self)
		imgSlotRight.LoadImage("d:/ymir work/ui/pattern/gauge_slot_right.tga")
		imgSlotRight.Show()
		imgSlotRight.SetPosition(width - self.SLOT_WIDTH, 0)

		imgSlotCenter = ExpandedImageBox()
		imgSlotCenter.SetParent(self)
		imgSlotCenter.LoadImage("d:/ymir work/ui/pattern/gauge_slot_center.tga")
		imgSlotCenter.Show()
		imgSlotCenter.SetRenderingRect(0.0, 0.0, float((width - self.SLOT_WIDTH*2) - self.SLOT_WIDTH) / self.SLOT_WIDTH, 0.0)
		imgSlotCenter.SetPosition(self.SLOT_WIDTH, 0)

		imgGaugeBack = ExpandedImageBox()
		imgGaugeBack.SetParent(self)
		imgGaugeBack.LoadImage("d:/ymir work/ui/pattern/gauge_yellow.tga")
		imgGaugeBack.Hide()
		imgGaugeBack.SetRenderingRect(0.0, 0.0, 0.0, 0.0)
		imgGaugeBack.SetPosition(self.GAUGE_TEMPORARY_PLACE, 0)

		imgGauge = ExpandedImageBox()
		imgGauge.SetParent(self)
		imgGauge.LoadImage("d:/ymir work/ui/pattern/gauge_" + color + ".tga")
		imgGauge.Show()
		imgGauge.SetRenderingRect(0.0, 0.0, 0.0, 0.0)
		imgGauge.SetPosition(self.GAUGE_TEMPORARY_PLACE, 0)

		imgSlotLeft.AddFlag("attach")
		imgSlotCenter.AddFlag("attach")
		imgGaugeBack.AddFlag("attach")
		imgSlotRight.AddFlag("attach")

		if app.BL_PARTY_UPDATE:
			imgSlotLeft.AddFlag("not_pick")
			imgSlotCenter.AddFlag("not_pick")
			imgSlotRight.AddFlag("not_pick")
			imgGauge.AddFlag("not_pick")

		self.imgLeft = imgSlotLeft
		self.imgCenter = imgSlotCenter
		self.imgRight = imgSlotRight
		self.imgGauge = imgGauge
		self.imgGaugeBack = imgGaugeBack

		self.SetSize(width, self.SLOT_HEIGHT)

	def SetPercentage(self, curValue, maxValue):

		# PERCENTAGE_MAX_VALUE_ZERO_DIVISION_ERROR
		if maxValue > 0.0:
			percentage = min(1.0, float(curValue)/float(maxValue))
		else:
			percentage = 0.0
		# END_OF_PERCENTAGE_MAX_VALUE_ZERO_DIVISION_ERROR

		self.__oldValue = self.__newValue
		self.__newValue = percentage

		gaugeSize = -1.0 + float(self.width - self.GAUGE_TEMPORARY_PLACE*2) * percentage / self.GAUGE_WIDTH
		self.imgGauge.SetRenderingRect(0.0, 0.0, gaugeSize, 0.0)

		self.SetPercentageBack(self.__oldValue, 1.0)

	def SetPercentageBack(self, curValue, maxValue):
		if not self.imgGaugeBack.IsShow():
			self.imgGaugeBack.Show()

		if maxValue > 0.0:
			percentage = min(1.0, float(curValue) / float(maxValue))
		else:
			percentage = 0.0

		gaugeSize = -1.0 + float(self.width - self.GAUGE_TEMPORARY_PLACE * 2) * percentage / self.GAUGE_WIDTH
		self.imgGaugeBack.SetRenderingRect(0.0, 0.0, gaugeSize, 0.0)

	def OnUpdate(self):
		if self.IsShow() and self.__oldValue > self.__newValue:
			self.__oldValue = self.__oldValue - 0.005
			self.SetPercentageBack(self.__oldValue, 1.0)

	'''
	if app.BL_PARTY_UPDATE:
		def GaugeImgBoxAddFlag(self, flag):
			self.imgLeft.AddFlag(flag)
			self.imgCenter.AddFlag(flag)
			self.imgRight.AddFlag(flag)
			self.imgGauge.AddFlag(flag)

	if app.ENABLE_POISON_GAUGE_EFFECT:
		def SetGaugeColor(self, color):
			if self.imgGauge:
				self.imgGauge.LoadImage("d:/ymir work/ui/pattern/gauge_" + color + ".tga")
	'''