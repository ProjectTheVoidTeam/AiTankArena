package cn.teamthevoid.AiTankArenaServer.game;

import cn.teamthevoid.AiTankArenaServer.Entity;
import cn.teamthevoid.AiTankArenaServer.UniqueIDEntity;
import cn.teamthevoid.AiTankArenaServer.message.operation.Tank;
import cn.teamthevoid.AiTankArenaServer.message.response.GameStage;

import java.util.List;

public abstract class Game extends UniqueIDEntity implements Entity {
    public abstract void join(Player player);

    public abstract void leave(Player player);

    public abstract List<Player> getPlayerList();

    public abstract GameState getGameState();

    public abstract void start();

    public GameStage stage = GameStage.WAITING;

    public abstract List<Tank> getAllTank();


}
