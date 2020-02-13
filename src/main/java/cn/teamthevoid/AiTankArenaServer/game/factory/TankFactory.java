package cn.teamthevoid.AiTankArenaServer.game.factory;


import cn.teamthevoid.AiTankArenaServer.game.Tank;
import cn.teamthevoid.AiTankArenaServer.game.Vector2D;
import cn.teamthevoid.AiTankArenaServer.game.impl.TankImpl;

public class TankFactory {
    public static Tank getInstance(Vector2D initPosition) {
        return new TankImpl(initPosition);
    }
}
