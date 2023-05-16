package com.bw.sophia

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.cloud.openfeign.EnableFeignClients

@SpringBootApplication()
@EnableFeignClients
class SophiaApplication

fun main(args: Array<String>) {
	runApplication<SophiaApplication>(*args)
}
