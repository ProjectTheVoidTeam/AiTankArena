
package cn.teamthevoid.AiTankArenaServer.handler;

import cn.teamthevoid.AiTankArenaServer.message.operation.Operation;
import cn.teamthevoid.AiTankArenaServer.message.operation.OperationType;
import cn.teamthevoid.AiTankArenaServer.message.response.Response;
import cn.teamthevoid.AiTankArenaServer.message.response.ServerInfo;
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
        var serverInfo = ServerInfo.newBuilder();
        serverInfo.setServerName("AI Tank Arena Testing Server");
        serverInfo.setWelcomeMessage("欢迎来到本服务器~嘤~~");
        serverInfo.setBuildId(10000);
        serverInfo.setVersion("0.0.1");
        response.setServerInfo(serverInfo);
        ctx.writeAndFlush(response.build());

    }
}