package cn.teamthevoid.AiTankArenaServer.game.factory;

import cn.teamthevoid.AiTankArenaServer.game.Game;
import cn.teamthevoid.AiTankArenaServer.game.impl.GameImpl;

public class GameFactory {
    public static Game getNewInstance() {
        return new GameImpl();
    }
}
