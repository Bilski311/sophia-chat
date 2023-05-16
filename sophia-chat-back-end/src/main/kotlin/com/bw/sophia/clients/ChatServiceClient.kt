package com.bw.sophia.clients

import org.springframework.cloud.openfeign.FeignClient

@FeignClient(name = "chatServiceClient", url = "http://example.com")
interface ChatServiceClient {
}