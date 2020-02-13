
package cn.teamthevoid.AiTankArenaServer.handler;

import cn.teamthevoid.AiTankArenaServer.game.factory.PlayerFactory;
import cn.teamthevoid.AiTankArenaServer.message.operation.Operation;
import cn.teamthevoid.AiTankArenaServer.message.operation.OperationType;
import cn.teamthevoid.AiTankArenaServer.message.operation.PlayerType;
import cn.teamthevoid.AiTankArenaServer.message.response.Response;
import cn.teamthevoid.AiTankArenaServer.message.response.Status;
import io.netty.channel.ChannelHandlerContext;
import lombok.extern.slf4j.Slf4j;

/**
 * Handles a server-side channel.
 */
@Slf4j
public class JoinGameHandler extends OperationInboundHandlerAdapter { // (1)
    @Override
    OperationType getOperationType() {
        return OperationType.JOIN;
    }
    @Override
    void channelRead(ChannelHandlerContext ctx, Operation operation) {
        var response = Response.newBuilder();
        var newPlayer = PlayerFactory.getNewInstance();
        newPlayer.isObserver = operation.getJoinRoomInfo().getType() == PlayerType.OBSERVER;
        newPlayer.playerName = operation.getJoinRoomInfo().getMyPlayerName();


        try {
            var id = serverState.joinRoom(operation.getJoinRoomInfo().getRoomId(), ctx.channel(), newPlayer);
            response.setStatus(Status.OK);
            response.setYourPlayerId(id);
        } catch (Exception e) {
            e.printStackTrace();
            response.setStatus(Status.NOT_FOUND);
        }

        ctx.channel().writeAndFlush(response.build());
    }

    @Override
    public void channelInactive(ChannelHandlerContext ctx) throws Exception {
        var player = serverState.getSelf(ctx.channel());
        serverState.exitRoom(player);
        log.info("玩家已退出:{}", player);
        super.channelInactive(ctx);
    }
}