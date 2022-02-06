// find:
typedef struct packet_target
{
	BYTE	header;
	DWORD	dwVID;
	BYTE	bHPPercent;
} TPacketGCTarget;

// replace with:
typedef struct packet_target
{
	BYTE	header;
	DWORD	dwVID;
	DWORD	dwHp;
	DWORD	dwHpMax;
} TPacketGCTarget;