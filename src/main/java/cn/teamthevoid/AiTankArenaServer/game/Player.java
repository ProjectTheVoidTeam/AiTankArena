package cn.teamthevoid.AiTankArenaServer.game;

import cn.teamthevoid.AiTankArenaServer.UniqueIDEntity;
import lombok.ToString;

@ToString(callSuper = true)
public abstract class Player extends UniqueIDEntity {
    public abstract boolean buyWeapon(Weapon weapon);

    public abstract void triggerWeapon(Weapon weapon);

    public String playerName;
    //观战玩家不能行动
    public boolean isObserver;
    public boolean isReady;

    //此回合是否操作结束
    public abstract void isActionDone();

}
