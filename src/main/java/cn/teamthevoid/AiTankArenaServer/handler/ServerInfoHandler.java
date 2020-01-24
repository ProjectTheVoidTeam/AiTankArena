
package cn.teamthevoid.AiTankArenaServer.handler;

import cn.teamthevoid.AiTankArenaServer.message.operation.Operation;
import cn.teamthevoid.AiTankArenaServer.message.operation.OperationType;
import cn.teamthevoid.AiTankArenaServer.message.response.Response;
import io.netty.channel.ChannelHandlerContext;

/**
 * Handles a server-side channel.
 */
public class ServerInfoHandler extends OperationInboundHandlerAdapter { // (1)
    @Override
    OperationType getOperationType() {
        return OperationType.SERVER_INFO;
    }

    @Override
    void channelRead(ChannelHandlerContext ctx, Operation operation) {
        var response = Response.newBuilder();
        response.setMessage("AiTankArenaServer version 0.0.1");
        ctx.writeAndFlush(response.build());

    }
}