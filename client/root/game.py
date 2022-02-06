## find:
	def SetHPTargetBoard(self, vid, hpPercentage):
		[...]

## replace with:
	def SetHPTargetBoard(self, vid, hpNow, hpMax):
		if vid != self.targetBoard.GetTargetVID():
			self.targetBoard.ResetTargetBoard()
			self.targetBoard.SetEnemyVID(vid)

		self.targetBoard.SetHP(hpNow, hpMax)
		self.targetBoard.Show()