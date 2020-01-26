package cn.teamthevoid.AiTankArenaServer.game;

import cn.teamthevoid.AiTankArenaServer.UniqueIDEntity;

public abstract class Player extends UniqueIDEntity {
    public abstract boolean buyWeapon(Weapon weapon);

    public abstract void triggerWeapon(Weapon weapon);

    //此回合是否操作结束
    public abstract void isDone();


}
