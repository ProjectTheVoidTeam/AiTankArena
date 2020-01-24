package cn.teamthevoid.AiTankArenaServer.game;

import cn.teamthevoid.AiTankArenaServer.UniqueIDEntity;

public abstract class Player extends UniqueIDEntity {
    public abstract boolean buyWeapon(Weapon weapon);

}
